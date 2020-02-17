%global packname  rfordummies
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Code Examples to Accompany the Book "R for Dummies"

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx 
Requires:         R-CRAN-openxlsx 

%description
Contains all the code examples in the book "R for Dummies" (2nd edition)
by Andrie de Vries and Joris Meys. You can view the table of contents as
well as the sample code for each chapter.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/chapters.R
%doc %{rlibdir}/%{packname}/cleanscripts.R
%doc %{rlibdir}/%{packname}/figures
%doc %{rlibdir}/%{packname}/makefile.R
%doc %{rlibdir}/%{packname}/scripts
%doc %{rlibdir}/%{packname}/stitch_dummies.R
%{rlibdir}/%{packname}/INDEX
