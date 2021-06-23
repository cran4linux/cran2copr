%global __brp_check_rpaths %{nil}
%global packname  countcolors
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          3%{?dist}%{?buildtag}
Summary:          Locates and Counts Pixels Within Color Range(s) in Images

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-colordistance 
BuildRequires:    R-tools 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
Requires:         R-CRAN-colordistance 
Requires:         R-tools 
Requires:         R-graphics 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 

%description
Counts colors within color range(s) in images, and provides a masked
version of the image with targeted pixels changed to a different color.
Output includes the locations of the pixels in the images, and the
proportion of the image within the target color range with optional
background masking. Users can specify multiple color ranges for masking.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
