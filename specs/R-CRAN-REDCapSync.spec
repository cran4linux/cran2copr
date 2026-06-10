%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  REDCapSync
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Encapsulated 'REDCap' Projects for Synchronized Data Pipelines

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-hoardr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-openxlsx2 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-redcapAPI 
BuildRequires:    R-CRAN-REDCapR 
BuildRequires:    R-CRAN-skimr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-hoardr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-openxlsx2 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-redcapAPI 
Requires:         R-CRAN-REDCapR 
Requires:         R-CRAN-skimr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-utils 

%description
Wraps dozens of 'REDCap' API endpoints into a standardized R6 object.
Research Electronic Data Capture ('REDCap') is a survey and database web
application software maintained by Vanderbilt University. It has a robust
application programming interface (API) utilized by several R packages.
'REDCapSync' uses 'redcapAPI' and 'REDCapR' behind-the-scenes to retrieve
all metadata, data, and log details for a project. To minimize unnecessary
server calls, the interim 'REDCap' log is analyzed and used to only update
necessary records. Furthermore, the user can define custom datasets that
save to a directory. Those datasets continue to refresh when projects are
synced.  Having a secure, standardized, API-efficient, project-agnostic R
object for 'REDCap' projects, streamlines downstream use in scripts,
functions, and shiny applications.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
