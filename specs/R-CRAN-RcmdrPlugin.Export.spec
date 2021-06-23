%global __brp_check_rpaths %{nil}
%global packname  RcmdrPlugin.Export
%global packver   0.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Export R Output to LaTeX or HTML

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.2.2
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-Rcmdr >= 2.2.2
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-Hmisc 

%description
Export Rcmdr output to LaTeX or HTML code. The plug-in was originally
intended to facilitate exporting Rcmdr output to formats other than ASCII
text and to provide R novices with an easy-to-use, easy-to-access
reference on exporting R objects to formats suited for printed output. The
package documentation contains several pointers on creating reports,
either by using conventional word processors or LaTeX/LyX.

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
%doc %{rlibdir}/%{packname}/LIMITATIONS
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
