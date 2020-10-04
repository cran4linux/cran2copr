%global packname  fieldRS
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Remote Sensing Field Work Tools

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-concaveman 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-concaveman 

%description
In remote sensing, designing a field campaign to collect ground-truth data
can be a challenging task. We need to collect representative samples while
accounting for issues such as budget constraints and limited accessibility
created by e.g. poor infrastructure. As suggested by Olofsson et al.
(2014) <doi:10.1016/j.rse.2014.02.015>, this demands the establishment of
best-practices to collect ground-truth data that avoid the waste of time
and funds. 'fieldRS' addresses this issue by helping scientists and
practitioners design field campaigns through the identification of
priority sampling sites, the extraction of potential sampling plots and
the conversion of plots into consistent training and validation samples
that can be used in e.g. land cover classification.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
