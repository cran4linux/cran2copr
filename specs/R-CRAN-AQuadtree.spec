%global packname  AQuadtree
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Confidentiality of Spatial Point Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-dplyr 

%description
Provides an automatic aggregation tool to manage point data privacy,
intended to be helpful for the production of official spatial data and for
researchers. The package pursues the data accuracy at the smallest
possible areas preventing individual information disclosure. The
methodology, based on hierarchical geographic data structures performs
aggregation and local suppression of point data to ensure privacy as
described in Lagonigro, R., Oller, R., Martori J.C. (2017)
<doi:10.2436/20.8080.02.55>. The data structures are created following the
guidelines for grid datasets from the European Forum for Geography and
Statistics.

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
