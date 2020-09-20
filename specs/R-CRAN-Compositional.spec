%global packname  Compositional
%global packver   4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-codalm 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-emplik 
BuildRequires:    R-CRAN-FlexDir 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-mixture 
BuildRequires:    R-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-Rfast2 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-stats 
Requires:         R-CRAN-codalm 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-emplik 
Requires:         R-CRAN-FlexDir 
Requires:         R-CRAN-foreach 
Requires:         R-MASS 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-mixture 
Requires:         R-nnet 
Requires:         R-parallel 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-Rfast2 
Requires:         R-CRAN-sn 
Requires:         R-stats 

%description
Regression, classification, contour plots, hypothesis testing and fitting
of distributions for compositional data are some of the functions
included. The standard textbook for such data is John Aitchison's (1986)
"The statistical analysis of compositional data". Relevant papers include
a) Tsagris M.T., Preston S. and Wood A.T.A. (2011) A data-based power
transformation for compositional data. Fourth International International
Workshop on Compositional Data Analysis. b) Tsagris M. (2014). The k-NN
algorithm for compositional data: a revised approach with and without zero
values present. Journal of Data Science, 12(3):519--534. c) Tsagris M.
(2015). A novel, divergence based, regression for compositional data.
Proceedings of the 28th Panhellenic Statistics Conference, 15-18 April
2015, Athens, Greece, 430--444. d) Tsagris M. (2015). Regression analysis
with compositional data containing zero values. Chilean Journal of
Statistics, 6(2):47--57. e) Tsagris M., Preston S. and Wood A.T.A. (2016).
Improved supervised classification for compositional data using the
alpha-transformation. Journal of Classification, 33(2):243--261.
<doi:10.1007/s00357-016-9207-5>. f) Tsagris M., Preston S. and Wood A.T.A.
(2017). Nonparametric hypothesis testing for equality of means on the
simplex. Journal of Statistical Computation and Simulation, 87(2):
406--422. <doi:10.1080/00949655.2016.1216554> g) Tsagris M. and Stewart C.
(2018). A Dirichlet regression model for compositional data with zeros.
Lobachevskii Journal of Mathematics, 39(3): 398--412.
<doi:10.1134/S1995080218030198>. h) Alenazi A. (2019). Regression for
compositional data with compositional data as predictor variables with or
without zero values. Journal of Data Science, 17(1): 219--238.
<doi:10.6339/JDS.201901_17(1).0010>. i) Tsagris M. and Stewart C. (2020).
A folded model for compositional data analysis. Australian and New Zealand
Journal of Statistics, 62(2):249--277. <doi:10.1111/anzs.12289>. j)
Tsagris M., Alenazi A. and Stewart C. (2020). The alpha-k-NN regression
for compositional data. <arXiv:2002.05137>. We further include functions
for percentages (or proportions).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
