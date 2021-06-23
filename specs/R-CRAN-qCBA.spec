%global __brp_check_rpaths %{nil}
%global packname  qCBA
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Quantitative Classification by Association Rules

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arules >= 1.6.6
BuildRequires:    R-CRAN-arc >= 1.2
BuildRequires:    R-CRAN-rJava >= 0.5.0
BuildRequires:    R-methods 
Requires:         R-CRAN-arules >= 1.6.6
Requires:         R-CRAN-arc >= 1.2
Requires:         R-CRAN-rJava >= 0.5.0
Requires:         R-methods 

%description
CBA postprocessing algorithm that creates smaller models for datasets
containing quantitative (numerical) attributes. Article describing QCBA is
published in Tomas Kliegr (2017) <arXiv:1711.10166>. The package can also
postprocess results of the SBRL package, which is no longer in CRAN, but
can be obtained from <https://github.com/cran/sbrl>.

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
