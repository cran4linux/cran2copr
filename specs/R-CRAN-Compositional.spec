%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Compositional
%global packver   6.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.8
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-Directional 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-emplik 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-FlexDir 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-mixture 
BuildRequires:    R-CRAN-mvhtests 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-pchc 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-regda 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-CRAN-Rnanoflann 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-stats 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-Directional 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-emplik 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-FlexDir 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-mixture 
Requires:         R-CRAN-mvhtests 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-pchc 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-regda 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-CRAN-Rnanoflann 
Requires:         R-CRAN-sn 
Requires:         R-stats 

%description
Regression, classification, contour plots, hypothesis testing and fitting
of distributions for compositional data are some of the functions
included. We further include functions for percentages (or proportions).
The standard textbook for such data is John Aitchison's (1986) "The
statistical analysis of compositional data". Relevant papers include: a)
Tsagris M.T., Preston S. and Wood A.T.A. (2011). "A data-based power
transformation for compositional data". Fourth International International
Workshop on Compositional Data Analysis. <doi:10.48550/arXiv.1106.1451> b)
Tsagris M. (2014). "The k-NN algorithm for compositional data: a revised
approach with and without zero values present". Journal of Data Science,
12(3): 519--534. <doi:10.6339/JDS.201407_12(3).0008>. c) Tsagris M.
(2015). "A novel, divergence based, regression for compositional data".
Proceedings of the 28th Panhellenic Statistics Conference, 15-18 April
2015, Athens, Greece, 430--444. <doi:10.48550/arXiv.1511.07600>. d)
Tsagris M. (2015). "Regression analysis with compositional data containing
zero values". Chilean Journal of Statistics, 6(2): 47--57.
<https://soche.cl/chjs/volumes/06/02/Tsagris(2015).pdf>. e) Tsagris M.,
Preston S. and Wood A.T.A. (2016). "Improved supervised classification for
compositional data using the alpha-transformation". Journal of
Classification, 33(2): 243--261. <doi:10.1007/s00357-016-9207-5>. f)
Tsagris M., Preston S. and Wood A.T.A. (2017). "Nonparametric hypothesis
testing for equality of means on the simplex". Journal of Statistical
Computation and Simulation, 87(2): 406--422.
<doi:10.1080/00949655.2016.1216554>. g) Tsagris M. and Stewart C. (2018).
"A Dirichlet regression model for compositional data with zeros".
Lobachevskii Journal of Mathematics, 39(3): 398--412.
<doi:10.1134/S1995080218030198>. h) Alenazi A. (2019). "Regression for
compositional data with compositional data as predictor variables with or
without zero values". Journal of Data Science, 17(1): 219--238.
<doi:10.6339/JDS.201901_17(1).0010>. i) Tsagris M. and Stewart C. (2020).
"A folded model for compositional data analysis". Australian and New
Zealand Journal of Statistics, 62(2): 249--277. <doi:10.1111/anzs.12289>.
j) Alenazi A. (2021). Alenazi, A. (2023). "A review of compositional data
analysis and recent advances". Communications in Statistics--Theory and
Methods, 52(16): 5535--5567. <doi:10.1080/03610926.2021.2014890>. k)
Alenazi A.A. (2022). "f-divergence regression models for compositional
data". Pakistan Journal of Statistics and Operation Research, 18(4):
867--882. <doi:10.18187/pjsor.v18i4.3969>. l) Tsagris M. and Stewart C.
(2022). "A Review of Flexible Transformations for Modeling Compositional
Data". In Advances and Innovations in Statistics and Data Science, pp.
225--234. <doi:10.1007/978-3-031-08329-7_10>. m) Tsagris M., Alenazi A.
and Stewart C. (2023). "Flexible non-parametric regression models for
compositional response data with zeros". Statistics and Computing,
33(106). <doi:10.1007/s11222-023-10277-5>. n) Tsagris. M. (2024).
"Constrained least squares simplicial-simplicial regression".
<arxiv:2403.19835>.

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
