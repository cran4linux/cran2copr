%global packname  pulsar
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          3%{?dist}
Summary:          Parallel Utilities for Lambda Selection along a RegularizationPath

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-Matrix 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-Matrix 

%description
Model selection for penalized graphical models using the Stability
Approach to Regularization Selection ('StARS'), with options for speed-ups
including Bounded StARS (B-StARS), batch computing, and other stability
metrics (e.g., graphlet stability G-StARS). Christian L. Müller, Richard
Bonneau, Zachary Kurtz (2016) <arXiv:1605.07072>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/config
%doc %{rlibdir}/%{packname}/CONTENT.Rmd
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/figure
%doc %{rlibdir}/%{packname}/gstars.bib
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
