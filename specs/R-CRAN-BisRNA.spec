%global packname  BisRNA
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of RNA Cytosine-5 Methylation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-MASS 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Bisulfite-treated RNA non-conversion in a set of samples is analysed as
follows : each sample's non-conversion distribution is identified to a
Poisson distribution. P-values adjusted for multiple testing are
calculated in each sample. Combined non-conversion P-values and standard
errors are calculated on the intersection of the set of samples. For
further details, see C Legrand, F Tuorto, M Hartmann, R Liebers, D Jakob,
M Helm and F Lyko (2017) <doi:10.1101/gr.210666.116>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/INDEX
