%global packname  IFC
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}
Summary:          Tools for Imaging Flow Cytometry

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.0
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-visNetwork 
Requires:         R-CRAN-Rcpp >= 0.10.0
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-png 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-jpeg 
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-KernSmooth 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-visNetwork 

%description
Contains several tools to treat imaging flow cytometry data from
'ImageStream®' and 'FlowSight®' cytometers ('Amnis®', part of 'Luminex®').
Provides an easy and simple way to read, write and subset .rif, .cif and
.daf files. Information such as masks, features, regions and populations
set within these files can be retrieved. In addition, raw data such as
images stored can also be accessed. Users, may hopefully increase their
productivity thanks to dedicated functions to extract, visualize and
export 'IFC' data. Toy data example can be installed through the 'IFCdata'
package of approximately 32 MB, which is available in a 'drat' repository
<https://gitdemont.github.io/IFCdata>. See file 'COPYRIGHTS' and file
'AUTHORS' for a list of copyright holders and authors.

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
