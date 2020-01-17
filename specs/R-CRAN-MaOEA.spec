%global packname  MaOEA
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Many Objective Evolutionary Algorithm

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-nsga2R 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-nsga2R 
Requires:         R-CRAN-lhs 
Requires:         R-nnet 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-e1071 
Requires:         R-MASS 
Requires:         R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-utils 

%description
A set of evolutionary algorithms to solve many-objective optimization.
Hybridization between the algorithms are also facilitated. Available
algorithms are: 'SMS-EMOA' <doi:10.1016/j.ejor.2006.08.008> 'NSGA-III'
<doi:10.1109/TEVC.2013.2281535> 'MO-CMA-ES' <doi:10.1145/1830483.1830573>
The following many-objective benchmark problems are also provided:
'DTLZ1'-'DTLZ4' from Deb, et al. (2001) <doi:10.1007/1-84628-137-7_6> and
'WFG4'-'WFG9' from Huband, et al. (2005) <doi:10.1109/TEVC.2005.861417>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
