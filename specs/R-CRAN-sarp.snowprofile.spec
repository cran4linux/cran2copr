%global packname  sarp.snowprofile
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Snow Profile Analysis for Snowpack and Avalanche Research

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-xml2 

%description
Analysis and plotting tools for snow profile data produced from manual
snowpack observations and physical snowpack models. The functions in this
package support snowpack and avalanche research by reading various formats
of data (including CAAML, SMET, generic csv, and outputs from the snow
cover model SNOWPACK), manipulate the data, and produce graphics such as
stratigraphy and time series profiles. Package developed by the Simon
Fraser University Avalanche Research Program
<http://www.avalancheresearch.ca>. Graphics apply visualization concepts
from Horton, Nowak, and Haegeli (2020, <doi:10.5194/nhess-20-1557-2020>).

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
