%global packname  worcs
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}
Summary:          Workflow for Open Reproducible Code in Science

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-prereg 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-prereg 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-digest 

%description
Create reproducible and transparent research projects in 'R', with a
minimal amount of code. This package is based on the Workflow for Open
Reproducible Code in Science (WORCS), a step-by-step procedure based on
best practices for Open Science. It includes an 'RStudio' project
template, several convenience functions, and all dependencies required to
make your project reproducible and transparent. WORCS is explained in the
tutorial paper by Van Lissa, Brandmaier, Brinkman, Lamprecht, Struiksma, &
Vreede (2020). <doi:10.17605/OSF.IO/ZCVBS>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
