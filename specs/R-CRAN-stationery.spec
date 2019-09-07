%global packname  stationery
%global packver   0.98.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.98.6
Release:          1%{?dist}
Summary:          Working Examples for Reproducible Research Documents

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kutils 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-kutils 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 

%description
Templates, guides, and scripts for writing documents in 'LaTeX' and 'R
markdown' to produce guides, slides, and reports. Special care is taken to
illustrate use of templates and customization opportunities. Challenges
and opportunities of 'HTML' output from 'R markdown' receive special
attention. Includes several vignettes to assist new users of literate
programming.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/theme
%{rlibdir}/%{packname}/INDEX
