%global packname  qtl2pleio
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Testing Pleiotropy in Multiparental Populations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gemma2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gemma2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-Matrix 
Requires:         R-CRAN-furrr 

%description
We implement an adaptation of Jiang & Zeng's (1995)
<https://www.genetics.org/content/140/3/1111> likelihood ratio test for
testing the null hypothesis of pleiotropy against the alternative
hypothesis, two separate quantitative trait loci. The test differs from
that in Jiang & Zeng (1995) <https://www.genetics.org/content/140/3/1111>
and that in Tian et al. (2016) <doi:10.1534/genetics.115.183624> in that
our test accommodates multiparental populations.

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
