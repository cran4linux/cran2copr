%global packname  descstatsr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Descriptive Univariate Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-moments 
Requires:         R-datasets 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-moments 

%description
It generates summary statistics on the input dataset using different
descriptive univariate statistical measures on entire data or at a group
level. Though there are other packages which does similar job but each of
these are deficient in one form or other, in the measures generated, in
treating numeric, character and date variables alike, no functionality to
view these measures on a group level or the way the output is represented.
Given the foremost role of the descriptive statistics in any of the
exploratory data analysis or solution development, there is a need for a
more constructive, structured and refined version over these packages.
This is the idea behind the package and it brings together all the
required descriptive measures to give an initial understanding of the data
quality, distribution in a faster,easier and elaborative way.The function
brings an additional capability to be able to generate these statistical
measures on the entire dataset or at a group level. It calculates measures
of central tendency (mean, median), distribution (count, proportion),
dispersion (min, max, quantile, standard deviation, variance) and shape
(skewness, kurtosis). Addition to these measures, it provides information
on the data type, count on no. of rows, unique entries and percentage of
missing entries. More importantly the measures are generated based on the
data types as required by them,rather than applying numerical measures on
character and data variables and vice versa. Output as a dataframe object
gives a very neat representation, which often is useful when working with
a large number of columns. It can easily be exported as csv and analyzed
further or presented as a summary report for the data.

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
%{rlibdir}/%{packname}/INDEX
