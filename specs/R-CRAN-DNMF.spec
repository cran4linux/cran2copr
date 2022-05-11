%global __brp_check_rpaths %{nil}
%global packname  DNMF
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Discriminant Non-Negative Matrix Factorization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-gplots 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Discriminant Non-Negative Matrix Factorization aims to extend the
Non-negative Matrix Factorization algorithm in order to extract features
that enforce not only the spatial locality, but also the separability
between classes in a discriminant manner. It refers to three article,
Zafeiriou, Stefanos, et al. "Exploiting discriminant information in
nonnegative matrix factorization with application to frontal face
verification." Neural Networks, IEEE Transactions on 17.3 (2006): 683-695.
Kim, Bo-Kyeong, and Soo-Young Lee. "Spectral Feature Extraction Using dNMF
for Emotion Recognition in Vowel Sounds." Neural Information Processing.
Springer Berlin Heidelberg, 2013. and Lee, Soo-Young, Hyun-Ah Song, and
Shun-ichi Amari. "A new discriminant NMF algorithm and its application to
the extraction of subtle emotional differences in speech." Cognitive
neurodynamics 6.6 (2012): 525-535.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
