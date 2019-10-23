%global packname  onewaytests
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          1%{?dist}
Summary:          One-Way Tests in Independent Groups Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-car 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nortest 
Requires:         R-graphics 
Requires:         R-utils 

%description
Performs one-way tests in independent groups designs; one-way analysis of
variance (ANOVA), Welch's heteroscedastic F test, Welch's heteroscedastic
F test with trimmed means and Winsorized variances, Brown-Forsythe test,
Alexander-Govern test, James second order test, Kruskal-Wallis test,
Scott-Smith test, Box F test and Johansen F test, Generalized tests
equivalent to Parametric Bootstrap and Fiducial tests. The package
performs pairwise comparisons and graphical approaches. Also, the package
includes Student's t test, Welch's t test and Mann-Whitney U test for two
samples. Moreover, it assesses variance homogeneity and normality of data
in each group via tests and plots (Dag et al., 2018,
<https://journal.r-project.org/archive/2018/RJ-2018-022/RJ-2018-022.pdf>).

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
%doc %{rlibdir}/%{packname}/citation
%{rlibdir}/%{packname}/INDEX
