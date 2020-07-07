%global packname  DeclareDesign
%global packver   0.22.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.22.0
Release:          3%{?dist}
Summary:          Declare and Diagnose Research Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomizr >= 0.20.0
BuildRequires:    R-CRAN-estimatr >= 0.20.0
BuildRequires:    R-CRAN-fabricatr >= 0.10.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-generics 
Requires:         R-CRAN-randomizr >= 0.20.0
Requires:         R-CRAN-estimatr >= 0.20.0
Requires:         R-CRAN-fabricatr >= 0.10.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-generics 

%description
Researchers can characterize and learn about the properties of research
designs before implementation using `DeclareDesign`. Ex ante declaration
and diagnosis of designs can help researchers clarify the strengths and
limitations of their designs and to improve their properties, and can help
readers evaluate a research strategy prior to implementation and without
access to results. It can also make it easier for designs to be shared,
replicated, and critiqued.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
