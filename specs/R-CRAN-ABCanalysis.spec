%global packname  ABCanalysis
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}
Summary:          Computed ABC Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-plotrix 

%description
For a given data set, the package provides a novel method of computing
precise limits to acquire subsets which are easily interpreted. Closely
related to the Lorenz curve, the ABC curve visualizes the data by
graphically representing the cumulative distribution function. Based on an
ABC analysis the algorithm calculates, with the help of the ABC curve, the
optimal limits by exploiting the mathematical properties pertaining to
distribution of analyzed items. The data containing positive values is
divided into three disjoint subsets A, B and C, with subset A comprising
very profitable values, i.e. largest data values ("the important few"),
subset B comprising values where the yield equals to the effort required
to obtain it, and the subset C comprising of non-profitable values, i.e.,
the smallest data sets ("the trivial many"). Package is based on "Computed
ABC Analysis for rational Selection of most informative Variables in
multivariate Data", PLoS One. Ultsch. A., Lotsch J. (2015)
<DOI:10.1371/journal.pone.0129767>.

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
