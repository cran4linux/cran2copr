%global packname  reprex
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Prepare Reproducible Example Code via the Clipboard

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 2.0.0
BuildRequires:    R-CRAN-clipr >= 0.4.0
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-callr >= 2.0.0
Requires:         R-CRAN-clipr >= 0.4.0
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-utils 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-withr 

%description
Convenience wrapper that uses the 'rmarkdown' package to render small
snippets of code to target formats that include both code and output. The
goal is to encourage the sharing of small, reproducible, and runnable
examples on code-oriented websites, such as <https://stackoverflow.com>
and <https://github.com>, or in email. The user's clipboard is the default
source of input code and the default target for rendered output. 'reprex'
also extracts clean, runnable R code from various common formats, such as
copy/paste from an R session.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/addins
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
