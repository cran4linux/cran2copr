%global packname  tikzDevice
%global packver   0.12.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.3
Release:          1%{?dist}
Summary:          R Graphics Output in LaTeX Format

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    texlive-pgf
Requires:         texlive-pgf
BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-filehash >= 2.3
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-filehash >= 2.3
Requires:         R-CRAN-png 

%description
Provides a graphics output device for R that records plots in a
LaTeX-friendly format. The device transforms plotting commands issued by R
functions into LaTeX code blocks. When included in a LaTeX document, these
blocks are interpreted with the help of 'TikZ'---a graphics package for
TeX and friends written by Till Tantau. Using the 'tikzDevice', the text
of R plots can contain LaTeX commands such as mathematical formula. The
device also allows arbitrary LaTeX code to be inserted into the output
stream.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
