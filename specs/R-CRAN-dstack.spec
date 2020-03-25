%global packname  dstack
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Publishing Interactive Plots

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-nanotime 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-nanotime 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-base64enc 

%description
A native R package that allows to publish, share and track revisions of
plots using your favorite plotting package, e.g. 'ggplot2'. It also
provides a kind of interactivity for such plots by specifying certain
parameters for any specific plot view. See <https://docs.dstack.ai> for
more information.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
