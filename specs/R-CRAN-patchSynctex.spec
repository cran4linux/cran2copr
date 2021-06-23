%global __brp_check_rpaths %{nil}
%global packname  patchSynctex
%global packver   0.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Communication Between Editor and Viewer for Literate Programs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-CRAN-stringr 

%description
This utility eases the debugging of literate documents ('noweb' files) by
patching the synchronization information (the '.synctex(.gz)' file)
produced by 'pdflatex' with concordance information produced by 'Sweave'
or 'knitr' and 'Sweave' or 'knitr' ; this allows for bilateral
communication between a text editor (visualizing the 'noweb' source) and a
viewer (visualizing the resultant 'PDF'), thus bypassing the intermediate
'TeX' file.

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
%{rlibdir}/%{packname}/INDEX
