%global packname  ztable
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Zebra-Striped Tables in LaTeX and HTML Formats

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-moonBook 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-moonBook 
Requires:         R-CRAN-scales 

%description
Makes zebra-striped tables (tables with alternating row colors) in LaTeX
and HTML formats easily from a data.frame, matrix, lm, aov, anova, glm,
coxph, nls, fitdistr, mytable and cbind.mytable objects.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ztableDemo
%{rlibdir}/%{packname}/INDEX
