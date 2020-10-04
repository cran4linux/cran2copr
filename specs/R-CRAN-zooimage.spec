%global packname  zooimage
%global packver   5.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.5.2
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Numerical Plankton Images

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-svMisc >= 0.9.67
BuildRequires:    R-CRAN-svDialogs >= 0.9.53
BuildRequires:    R-CRAN-mlearning 
BuildRequires:    R-CRAN-filehash 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-tools 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-svMisc >= 0.9.67
Requires:         R-CRAN-svDialogs >= 0.9.53
Requires:         R-CRAN-mlearning 
Requires:         R-CRAN-filehash 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-CRAN-tiff 
Requires:         R-utils 
Requires:         R-CRAN-digest 
Requires:         R-tools 
Requires:         R-MASS 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 

%description
A free (open source) solution for analyzing digital images of plankton. In
combination with ImageJ, a free image analysis system, it processes
digital images, measures individuals, trains for automatic classification
of taxa, and finally, measures plankton samples (abundances, total and
partial size spectra or biomasses, etc.).

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
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/gui
%doc %{rlibdir}/%{packname}/planktonSorter
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
