%global packname  corx
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Create and Format Correlation Matrices

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-ggcorrplot 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-moments 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-ggcorrplot 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-moments 

%description
Create correlation (or partial correlation) matrices. Correlation matrices
are formatted with significance stars based on user preferences. Matrices
of coefficients, p-values, and number of pairwise observations are
returned. Send resultant formatted matrices to the clipboard to be pasted
into excel and other programs. A plot method allows users to visualize
correlation matrices created with 'corx'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
