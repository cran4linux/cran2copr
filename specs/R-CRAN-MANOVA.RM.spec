%global packname  MANOVA.RM
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Resampling-Based Analysis of Multivariate Data and RepeatedMeasures Designs

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.43
BuildRequires:    R-CRAN-plotrix >= 3.5.12
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-magic >= 1.5.6
BuildRequires:    R-Matrix >= 1.2.2
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-data.table 
Requires:         R-MASS >= 7.3.43
Requires:         R-CRAN-plotrix >= 3.5.12
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-magic >= 1.5.6
Requires:         R-Matrix >= 1.2.2
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-data.table 

%description
Implemented are various tests for semi-parametric repeated measures and
general MANOVA designs that do neither assume multivariate normality nor
covariance homogeneity, i.e., the procedures are applicable for a wide
range of general multivariate factorial designs. In addition to asymptotic
inference methods, novel bootstrap and permutation approaches are
implemented as well. These provide more accurate results in case of small
to moderate sample sizes. Furthermore, post-hoc comparisons are provided
for the multivariate analyses. Friedrich, S., Konietschke, F. and Pauly,
M. (2018) <arXiv:1801.08002>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
