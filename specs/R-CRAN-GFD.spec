%global packname  GFD
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Tests for General Factorial Designs

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.43
BuildRequires:    R-CRAN-plotrix >= 3.5.12
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-magic >= 1.5.6
BuildRequires:    R-Matrix >= 1.2.2
BuildRequires:    R-methods 
Requires:         R-MASS >= 7.3.43
Requires:         R-CRAN-plotrix >= 3.5.12
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-magic >= 1.5.6
Requires:         R-Matrix >= 1.2.2
Requires:         R-methods 

%description
Implemented are the Wald-type statistic, a permuted version thereof as
well as the ANOVA-type statistic for general factorial designs, even with
non-normal error terms and/or heteroscedastic variances, for crossed
designs with an arbitrary number of factors and nested designs with up to
three factors.

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
