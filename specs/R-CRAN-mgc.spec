%global packname  mgc
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          2%{?dist}%{?buildtag}
Summary:          Multiscale Graph Correlation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-raster 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-abind 
Requires:         R-boot 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-raster 

%description
Multiscale Graph Correlation (MGC) is a framework developed by Vogelstein
et al. (2019) <DOI:10.7554/eLife.41690> that extends global correlation
procedures to be multiscale; consequently, MGC tests typically require far
fewer samples than existing methods for a wide variety of dependence
structures and dimensionalities, while maintaining computational
efficiency. Moreover, MGC provides a simple and elegant multiscale
characterization of the potentially complex latent geometry underlying the
relationship.

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

%files
%{rlibdir}/%{packname}
