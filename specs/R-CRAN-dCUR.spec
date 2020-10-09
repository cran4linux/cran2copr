%global packname  dCUR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Dimension Reduction with Dynamic CUR

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stackoverflow 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-parallel 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stackoverflow 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rdpack 

%description
Dynamic CUR (dCUR) boosts the CUR decomposition (Mahoney MW., Drineas P.
(2009) <doi:10.1073/pnas.0803205106>) varying the k, the number of columns
and rows used, and its final purposes to help find the stage, which
minimizes the relative error to reduce matrix dimension. The goal of CUR
Decomposition is to give a better interpretation of the matrix
decomposition employing proper variable selection in the data matrix, in a
way that yields a simplified structure. Its origins come from analysis in
genetics. The goal of this package is to show an alternative to variable
selection (columns) or individuals (rows). The idea proposed consists of
adjusting the probability distributions to the leverage scores and
selecting the best columns and rows that minimize the reconstruction error
of the matrix approximation ||A-CUR||. It also includes a method that
recalibrates the relative importance of the leverage scores according to
an external variable of the user's interest.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
