%global packname  GapAnalysis
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Conservation Indicators using Spatial Information

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-base >= 3.5
BuildRequires:    R-utils >= 3.5
BuildRequires:    R-methods >= 3.5
BuildRequires:    R-CRAN-raster >= 3.0
BuildRequires:    R-CRAN-tmap >= 2.3
BuildRequires:    R-CRAN-rmarkdown >= 2.1
BuildRequires:    R-CRAN-geosphere >= 1.5
BuildRequires:    R-CRAN-sp >= 1.4.1
BuildRequires:    R-CRAN-fasterize >= 1.0.0
BuildRequires:    R-CRAN-sf >= 0.8
BuildRequires:    R-CRAN-dataverse >= 0.2.0
BuildRequires:    R-CRAN-data.table 
Requires:         R-base >= 3.5
Requires:         R-utils >= 3.5
Requires:         R-methods >= 3.5
Requires:         R-CRAN-raster >= 3.0
Requires:         R-CRAN-tmap >= 2.3
Requires:         R-CRAN-rmarkdown >= 2.1
Requires:         R-CRAN-geosphere >= 1.5
Requires:         R-CRAN-sp >= 1.4.1
Requires:         R-CRAN-fasterize >= 1.0.0
Requires:         R-CRAN-sf >= 0.8
Requires:         R-CRAN-dataverse >= 0.2.0
Requires:         R-CRAN-data.table 

%description
Supports the assessment of the degree of conservation of taxa in
conservation systems, both in ex situ (in genebanks, botanical gardens,
and other repositories) and in situ (in protected natural areas). Methods
are described in Khoury et al. (2019) <doi:10.1016/j.ecolind.2018.11.016>,
Khoury et al. (2019) <doi:10.1111/DDI.13008>, Castaneda-Alvarez et al.
(2016) <doi:10.1038/nplants.2016.22>, and Ramirez-Villegas et al. (2010)
<doi:10.1371/journal.pone.0013497>.

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
