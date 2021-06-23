%global __brp_check_rpaths %{nil}
%global packname  vocaldia
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          3%{?dist}%{?buildtag}
Summary:          Create and Manipulate Vocalisation Diagrams

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Create adjacency matrices of vocalisation graphs from dataframes
containing sequences of speech and silence intervals, transforming these
matrices into Markov diagrams, and generating datasets for classification
of these diagrams by 'flattening' them and adding global properties
(functionals) etc.  Vocalisation diagrams date back to early work in
psychiatry (Jaffe and Feldstein, 1970) and social psychology (Dabbs and
Ruback, 1987) but have only recently been employed as a data
representation method for machine learning tasks including meeting
segmentation (Luz, 2012) <doi:10.1145/2328967.2328970> and classification
(Luz, 2013) <doi:10.1145/2522848.2533788>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
