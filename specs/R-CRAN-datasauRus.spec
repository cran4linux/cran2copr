%global packname  datasauRus
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}
Summary:          Datasets from the Datasaurus Dozen

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
The Datasaurus Dozen is a set of datasets with the same summary
statistics. They retain the same summary statistics despite having
radically different distributions. The datasets represent a larger and
quirkier object lesson that is typically taught via Anscombe's Quartet
(available in the 'datasets' package). Anscombe's Quartet contains four
very different distributions with the same summary statistics and as such
highlights the value of visualisation in understanding data, over and
above summary statistics. As well as being an engaging variant on the
Quartet, the data is generated in a novel way. The simulated annealing
process used to derive datasets from the original Datasaurus is detailed
in "Same Stats, Different Graphs: Generating Datasets with Varied
Appearance and Identical Statistics through Simulated Annealing"
<doi:10.1145/3025453.3025912>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
