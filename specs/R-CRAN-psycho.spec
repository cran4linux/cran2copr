%global packname  psycho
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          2%{?dist}
Summary:          Efficient and Publishing-Oriented Workflow for PsychologicalScience

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-parameters 
BuildRequires:    R-CRAN-performance 
BuildRequires:    R-CRAN-effectsize 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-parameters 
Requires:         R-CRAN-performance 
Requires:         R-CRAN-effectsize 

%description
The main goal of the psycho package is to provide tools for psychologists,
neuropsychologists and neuroscientists, to facilitate and speed up the
time spent on data analysis. It aims at supporting best practices and
tools to format the output of statistical methods to directly paste them
into a manuscript, ensuring statistical reporting standardization and
conformity.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
