%global packname  Digiroo2
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          An application programming interface for generating null modelsof social contacts based on individuals' space use

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-spdep 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-spdep 

%description
Digiroo2 is an R package developed by researchers at the University of
Queensland to investigate association patterns and social structure in
wild animal populations. Proximity between individuals is generally
considered to be an appropriate proxy for associations and pairwise
association indices are the most widely used technique for analysing
animal social structure. However, little attention is given to identifying
how patterns of spatial overlap affect these association patterns. For
example, do individuals associate randomly with others with whom they
share home ranges, or do some individuals go out of their way to associate
with or avoid particular individuals? This program builds a null model of
random associations based on an individual's space use determined using
home range methodologies. Random points may be generated within a
specified home range contour or according to the Utilization Distribution
(UD). Expected associations of individuals are extracted based on
probability of occurrence and the proximity between home range weighted
random points. Association matrices can be generated from multiple
permutations for analysis using SOCPROG 2.4 (Whitehead 2009) to create
'expected' pairwise half-weight association indices (HWIs). These may be
compared with the 'observed' HWIs from field observations to reveal
whether pairs of animals associate more (= attraction) or less (=
avoidance) than expected by chance.

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
%{rlibdir}/%{packname}/INDEX
