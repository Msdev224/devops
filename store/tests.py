from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Product, Variation
from category.models import Category
from decimal import Decimal

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Créer une catégorie pour les tests
        cls.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )
        # Créer un produit pour les tests
        cls.product = Product.objects.create(
            product_name='Test Product',
            slug='test-product',
            description='A test product',
            price=Decimal('19.99'),
            image='photos/products/test.jpg',
            stock=10,
            is_available=True,
            category=cls.category
        )

    def test_product_creation(self):
        """Teste la création d'un produit"""
        product = self.product
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(product.__str__(), 'Test Product')
        self.assertEqual(product.product_name, 'Test Product')
        self.assertEqual(product.slug, 'test-product')
        self.assertEqual(product.price, Decimal('19.99'))
        self.assertEqual(product.stock, 10)
        self.assertTrue(product.is_available)
        self.assertEqual(product.category, self.category)

    def test_product_get_url(self):
        """Teste la méthode get_url"""
        product = self.product
        expected_url = reverse('product_detail', args=['test-category', 'test-product'])
        self.assertEqual(product.get_url(), expected_url)

    def test_product_meta(self):
        """Teste les options Meta"""
        meta = Product._meta
        self.assertEqual(meta.verbose_name, 'product')
        self.assertEqual(meta.verbose_name_plural, 'products')

    def test_product_unique_name_and_slug(self):
        """Teste l'unicité du nom et du slug"""
        with self.assertRaises(Exception):
            Product.objects.create(
                product_name='Test Product',  # Même nom
                slug='different-slug',
                price=Decimal('29.99'),
                image='photos/products/test2.jpg',
                stock=5,
                category=self.category
            )
        with self.assertRaises(Exception):
            Product.objects.create(
                product_name='Different Product',
                slug='test-product',  # Même slug
                price=Decimal('29.99'),
                image='photos/products/test2.jpg',
                stock=5,
                category=self.category
            )


class VariationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Créer une catégorie et un produit
        cls.category = Category.objects.create(
            name='Test Category',
            slug='test-category'
        )
        cls.product = Product.objects.create(
            product_name='Test Product',
            slug='test-product',
            price=Decimal('19.99'),
            image='photos/products/test.jpg',
            stock=10,
            category=cls.category
        )
        # Créer des variations
        cls.color_variation = Variation.objects.create(
            product=cls.product,
            variation_category='color',
            variation_value='Red',
            is_active=True
        )
        cls.size_variation = Variation.objects.create(
            product=cls.product,
            variation_category='size',
            variation_value='Medium',
            is_active=True
        )
        cls.inactive_variation = Variation.objects.create(
            product=cls.product,
            variation_category='color',
            variation_value='Blue',
            is_active=False
        )

    def test_variation_creation(self):
        """Teste la création d'une variation"""
        variation = self.color_variation
        self.assertTrue(isinstance(variation, Variation))
        self.assertEqual(variation.__str__(), 'Red')
        self.assertEqual(variation.variation_category, 'color')
        self.assertEqual(variation.variation_value, 'Red')
        self.assertTrue(variation.is_active)
        self.assertEqual(variation.product, self.product)

    def test_variation_manager_colors(self):
        """Teste le manager pour les variations de couleur"""
        colors = Variation.objects.colors()
        self.assertIn(self.color_variation, colors)
        self.assertNotIn(self.size_variation, colors)
        self.assertNotIn(self.inactive_variation, colors)
        self.assertEqual(colors.count(), 1)

    def test_variation_manager_sizes(self):
        """Teste le manager pour les variations de taille"""
        sizes = Variation.objects.sizes()
        self.assertIn(self.size_variation, sizes)
        self.assertNotIn(self.color_variation, sizes)
        self.assertNotIn(self.inactive_variation, sizes)
        self.assertEqual(sizes.count(), 1)

    def test_variation_category_choices(self):
        """Teste les choix de variation_category"""
        variation = self.color_variation
        field = Variation._meta.get_field('variation_category')
        self.assertEqual(field.choices, [('color', 'color'), ('size', 'size')])