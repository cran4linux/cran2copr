%global __brp_check_rpaths %{nil}
%global packname  ART
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Aligned Rank Transform for Nonparametric Factorial Analysis

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-car 
Requires:         R-stats 
Requires:         R-CRAN-car 

%description
An implementation of the Aligned Rank Transform technique for factorial
analysis (see references below for details) including models with missing
terms (unsaturated factorial models). The function first computes a
separate aligned ranked response variable for each effect of the
user-specified model, and then runs a classic ANOVA on each of the aligned
ranked responses. For further details, see Higgins, J. J. and Tashtoush,
S. (1994). An aligned rank transform test for interaction. Nonlinear World
1 (2), pp. 201-211. Wobbrock, J.O., Findlater, L., Gergle, D. and
Higgins,J.J. (2011). The Aligned Rank Transform for nonparametric
factorial analyses using only ANOVA procedures. Proceedings of the ACM
Conference on Human Factors in Computing Systems (CHI '11). New York: ACM
Press, pp. 143-146. <doi:10.1145/1978942.1978963>.

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
