%global packname  colocr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Conduct Co-Localization Analysis of Fluorescence MicroscopyImages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-magrittr 

%description
Automate the co-localization analysis of fluorescence microscopy images.
Selecting regions of interest, extract pixel intensities from the image
channels and calculate different co-localization statistics. The methods
implemented in this package are based on Dunn et al. (2011)
<doi:10.1152/ajpcell.00462.2010>.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/colocr_app
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
