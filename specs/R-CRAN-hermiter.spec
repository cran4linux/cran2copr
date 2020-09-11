%global packname  hermiter
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Sequential and Batch Estimation of Probability Density Functions, Cumulative Distribution Functions and Quantiles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-methods 

%description
Facilitates estimation of the full probability density function,
cumulative distribution function and quantile function using Hermite
series based estimators. These estimators are particularly useful in the
sequential setting (both stationary and non-stationary) and one-pass batch
estimation setting for large data sets. Based on: Stephanou, Michael,
Varughese, Melvin and Iain Macdonald. "Sequential quantiles via Hermite
series density estimation." Electronic Journal of Statistics 11.1 (2017):
570-607 <doi:10.1214/17-EJS1245> and Stephanou, Michael and Varughese,
Melvin. "On the properties of Hermite series based distribution function
estimators." Metrika (2020) <doi:10.1007/s00184-020-00785-z>.

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
