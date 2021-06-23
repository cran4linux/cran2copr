%global __brp_check_rpaths %{nil}
%global packname  ImaginR
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Delimit and Characterize Color Phenotype of the Pearl Oyster

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jpeg 
Requires:         R-CRAN-imager 
Requires:         R-grDevices 
Requires:         R-CRAN-jpeg 

%description
The pearl oyster, Pinctada margaritifera (Linnaeus, 1758), represents the
second economic resource of French Polynesia. It is one of the only
bivalves expressing a large varied range of inner shell color, & by
correlation, of pearl color. This phenotypic variability is partly under
genetic control, but also under environmental influence. With ImaginR,
it's now possible to delimit the color phenotype of the pearl oyster's
inner shell and to characterize their color variations (by the HSV color
code system) with pictures.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
