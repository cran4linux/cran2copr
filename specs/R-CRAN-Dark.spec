%global packname  Dark
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          3%{?dist}
Summary:          The Analysis of Dark Adaptation Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 

%description
The recovery of visual sensitivity in a dark environment is known as dark
adaptation. In a clinical or research setting the recovery is typically
measured after a dazzling flash of light and can be described by the
Mahroo, Lamb and Pugh (MLP) model of dark adaptation. The functions in
this package take dark adaptation data and use nonlinear regression to
find the parameters of the model that 'best' describe the data. They do
this by firstly, generating rapid initial objective estimates of data
adaptation parameters, then a multi-start algorithm is used to reduce the
possibility of a local minimum. There is also a bootstrap method to
calculate parameter confidence intervals. The functions rely upon a 'dark'
list or object. This object is created as the first step in the workflow
and parts of the object are updated as it is processed.

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
