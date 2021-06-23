%global __brp_check_rpaths %{nil}
%global packname  rreg
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization for Norwegian Health Quality Registries

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-directlabels 
Requires:         R-grid 
Requires:         R-stats 

%description
Assists for presentation and visualization of data from the Norwegian
Health Quality Registries following the standardization based on the
requirement specified by the National Service for Health Quality
Registries. This requirement can be accessed from
(<https://www.kvalitetsregistre.no/resultater-til-publisering-pa-nett>).
Unfortunately the website is only available in Norwegian.

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
