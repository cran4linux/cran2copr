%global packname  rcicr
%global packver   0.3.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4.1
Release:          1%{?dist}
Summary:          Reverse-Correlation Image-Classification Toolbox

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-aspace 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-aspace 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-scales 
Requires:         R-utils 

%description
Functions to generate stimuli and analyze data of reverse correlation
image classification experiments (psychophysical tasks aimed at
visualizing cognitive mental representations of faces).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
