%global __brp_check_rpaths %{nil}
%global packname  MetaAnalyser
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          An Interactive Visualisation of Meta-Analysis as a PhysicalWeighing Machine

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DT >= 0.1.40
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggvis 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-DT >= 0.1.40
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggvis 
Requires:         R-CRAN-rstudioapi 

%description
An interactive application to visualise meta-analysis data as a physical
weighing machine. The interface is based on the Shiny web application
framework, though can be run locally and with the user's own data.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
