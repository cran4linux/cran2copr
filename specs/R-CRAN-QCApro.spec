%global __brp_check_rpaths %{nil}
%global packname  QCApro
%global packver   1.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Advanced Functionality for Performing and Evaluating QualitativeComparative Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-utils 
Requires:         R-CRAN-lpSolve 
Requires:         R-utils 

%description
Provides advanced functionality for performing configurational comparative
research with Qualitative Comparative Analysis (QCA), including crisp-set,
multi-value, and fuzzy-set QCA. It also offers advanced tools for
sensitivity diagnostics and methodological evaluations of QCA.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
