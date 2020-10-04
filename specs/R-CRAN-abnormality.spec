%global packname  abnormality
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Measure a Subject's Abnormality with Respect to a ReferencePopulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.0
BuildRequires:    R-Matrix 
Requires:         R-MASS >= 7.3.0
Requires:         R-Matrix 

%description
Contains the functions to implement the methodology and considerations
laid out by Marks et al. in the manuscript Measuring Abnormality in High
Dimensional Spaces: Applications in Biomechanical Gait Analysis. As of
2/27/2018 this paper has been submitted and is under scientific review.
Using high-dimensional datasets to measure a subject’s overall level of
abnormality as compared to a reference population is often needed in
outcomes research. Utilizing applications in instrumented gait analysis,
that article demonstrates how using data that is inherently
non-independent to measure overall abnormality may bias results. A
methodology is introduced to address this bias to accurately measure
overall abnormality in high dimensional spaces. While this methodology is
in line with previous literature, it differs in two major ways.
Advantageously, it can be applied to datasets in which the number of
observations is less than the number of features/variables, and it can be
abstracted to practically any number of domains or dimensions. After
applying the proposed methodology to the original data, the researcher is
left with a set of uncorrelated variables (i.e. principal components) with
which overall abnormality can be measured without bias. Different
considerations are discussed in that article in deciding the appropriate
number of principal components to keep and the aggregate distance measure
to utilize.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
