%global __brp_check_rpaths %{nil}
%global packname  patchDVI
%global packver   1.10.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10.1
Release:          3%{?dist}%{?buildtag}
Summary:          Package to Patch '.dvi' or '.synctex' Files

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-utils 
Requires:         R-tools 

%description
Functions to patch specials in '.dvi' files, or entries in '.synctex'
files.  Works with concordance=TRUE in Sweave or knitr to link sources to
previews.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/todo.txt
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
