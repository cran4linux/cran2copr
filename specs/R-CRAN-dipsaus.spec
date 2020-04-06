%global packname  dipsaus
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}
Summary:          A Dipping Sauce for Data Analysis and Visualizations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fastmap 
BuildRequires:    R-CRAN-base64url 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-txtq 
BuildRequires:    R-CRAN-synchronicity 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-startup 
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-stringr 
Requires:         R-parallel 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fastmap 
Requires:         R-CRAN-base64url 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-txtq 
Requires:         R-CRAN-synchronicity 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-startup 

%description
Works as "add-ons" to packages like 'shiny', 'future', as well as 'rlang',
and provides utility functions. Just like dipping sauce adding flavors to
potato chips or pita bread, 'dipsaus' for data analysis and visualizations
adds handy functions and enhancements to popular packages. The goal is to
provide simple solutions that are frequently asked for online, such as how
to synchronize 'shiny' inputs without freezing the app, or how to get
memory size on 'Linux' or 'MacOS' system. The enhancements roughly fall
into these four categories: 1. 'shiny' input widgets; 2. high-performance
computing using 'RcppParallel' and 'future' package; 3. modify R calls and
convert among numbers, strings, and other objects. 4. utility functions to
get system information such like CPU chipset, memory limit, etc.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny-addons
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
