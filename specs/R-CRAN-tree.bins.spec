%global packname  tree.bins
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Recategorization of Factor Variables by Decision Tree Leaves

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-rpart >= 4.1.11
BuildRequires:    R-CRAN-data.table >= 1.10.4.3
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-rpart.utils >= 0.5
Requires:         R-rpart >= 4.1.11
Requires:         R-CRAN-data.table >= 1.10.4.3
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-rpart.utils >= 0.5

%description
Provides users the ability to categorize categorical variables dependent
on a response variable. It creates a decision tree by using one of the
categorical variables (class factor) and the selected response variable.
The decision tree is created from the rpart() function from the 'rpart'
package. The rules from the leaves of the decision tree are extracted, and
used to recategorize the appropriate categorical variable (predictor).
This step is performed for each of the categorical variables that is fed
into the data component of the function. Only variables containing more
than 2 factor levels will be considered in the function. The final output
generates a data set containing the recategorized variables or a list
containing a mapping table for each of the candidate variables. For more
details see T. Hastie et al (2009, ISBN: 978-0-387-84857-0).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
