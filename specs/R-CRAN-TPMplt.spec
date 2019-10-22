%global packname  TPMplt
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Tool-Kit for Dynamic Materials Model and Thermal Processing Maps

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-VBTree 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rowr 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-dlm 
Requires:         R-CRAN-VBTree 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-e1071 
Requires:         R-grDevices 
Requires:         R-CRAN-rowr 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-directlabels 
Requires:         R-utils 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-dlm 

%description
Provides a simple approach for constructing dynamic materials modeling
suggested by Prasad and Gegel <doi:10.1007/BF02664902>. It can easily
generate various processing-maps based on this model as well. The
calculation result in this package contains full materials constants,
information about power dissipation efficiency factor, and rheological
properties, can be exported completely also, through which further
analysis and customized plots will be applicable as well.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
