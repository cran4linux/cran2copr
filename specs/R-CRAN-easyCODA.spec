%global packname  easyCODA
%global packver   0.34.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.34.3
Release:          1%{?dist}%{?buildtag}
Summary:          Compositional Data Analysis in Practice

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan >= 2.3
BuildRequires:    R-CRAN-ca >= 0.7
BuildRequires:    R-CRAN-ellipse >= 0.4.1
Requires:         R-CRAN-vegan >= 2.3
Requires:         R-CRAN-ca >= 0.7
Requires:         R-CRAN-ellipse >= 0.4.1

%description
Univariate and multivariate methods for compositional data analysis, based
on logratios. The package implements the approach in the book
Compositional Data Analysis in Practice by Michael Greenacre (2018), where
accent is given to simple pairwise logratios. Selection can be made of
logratios that account for a maximum percentage of logratio variance.
Various multivariate analyses of logratios are included in the package.

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
